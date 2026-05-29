import { createReadStream } from "node:fs";
import fs from "node:fs/promises";
import path from "node:path";

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1")), "..");
const credentialsPath = path.resolve(process.env.YOUTUBE_CLIENT_SECRET_PATH || "C:/Users/aaron/.barz/secrets/youtube-client-secret.json");
const tokenPath = path.resolve(process.env.YOUTUBE_TOKEN_PATH || "C:/Users/aaron/.barz/artifacts/youtube-schedule/token.json");
const videoPath = path.resolve(root, "artifacts/swarmops-case-commander-narrated-demo.mp4");
const metadataPath = path.resolve(root, "docs/youtube-devpost-metadata.md");
const outputPath = path.resolve(root, "artifacts/youtube-upload.json");

const uploadScopes = [
  "https://www.googleapis.com/auth/youtube.upload",
  "https://www.googleapis.com/auth/youtube",
  "https://www.googleapis.com/auth/youtubepartner",
  "https://www.googleapis.com/auth/youtube.force-ssl",
];

function requireString(value, label) {
  if (typeof value !== "string" || !value.trim()) {
    throw new Error(`${label} is missing.`);
  }
  return value;
}

function redact(input) {
  return String(input || "")
    .replace(/(Bearer\s+)[A-Za-z0-9._~+/=-]+/gi, "$1[REDACTED]")
    .replace(/("(?:access_token|refresh_token|client_secret|client_id)"\s*:\s*")[^"]+(")/gi, "$1[REDACTED]$2")
    .replace(/\bya29\.[A-Za-z0-9._~+/=-]+/g, "[REDACTED]");
}

async function readJson(filePath, label) {
  const raw = await fs.readFile(filePath, "utf8");
  try {
    return JSON.parse(raw);
  } catch {
    throw new Error(`${label} is not valid JSON.`);
  }
}

function getOAuthClient(credentials) {
  const client = credentials.installed || credentials.web;
  if (!client) throw new Error("YouTube OAuth credentials must contain installed or web client data.");
  return {
    clientId: requireString(client.client_id, "YouTube client_id"),
    clientSecret: requireString(client.client_secret, "YouTube client_secret"),
    tokenUri: client.token_uri || "https://oauth2.googleapis.com/token",
  };
}

function tokenHasUploadScope(token) {
  if (!token.scope) return true;
  const scopes = new Set(String(token.scope).split(/\s+/).filter(Boolean));
  return uploadScopes.some((scope) => scopes.has(scope));
}

async function parseJsonResponse(response, action) {
  const text = await response.text();
  const payload = text ? JSON.parse(text) : {};
  if (response.ok) return payload;
  const message = payload?.error?.message || text || response.statusText;
  const reason = payload?.error?.errors?.map((item) => item.reason).filter(Boolean).join(", ");
  throw new Error(`${action} failed (${response.status} ${response.statusText}${reason ? `; reason=${reason}` : ""}): ${redact(message)}`);
}

async function getAccessToken() {
  const credentials = await readJson(credentialsPath, "YouTube OAuth credentials");
  const token = await readJson(tokenPath, "YouTube OAuth token");
  const client = getOAuthClient(credentials);

  if (!tokenHasUploadScope(token)) {
    throw new Error(`Saved YouTube token is missing upload scope. Re-authorize with one of: ${uploadScopes.join(", ")}`);
  }

  if (token.access_token && token.expiry_date && token.expiry_date > Date.now() + 60_000) {
    return token.access_token;
  }

  const body = new URLSearchParams({
    client_id: client.clientId,
    client_secret: client.clientSecret,
    refresh_token: requireString(token.refresh_token, "YouTube refresh_token"),
    grant_type: "refresh_token",
  });
  const response = await fetch(client.tokenUri, {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body,
  });
  const payload = await parseJsonResponse(response, "YouTube token refresh");
  token.access_token = requireString(payload.access_token, "YouTube access_token");
  token.expiry_date = Date.now() + Number(payload.expires_in || 3600) * 1000;
  token.scope = payload.scope || token.scope;
  token.token_type = payload.token_type || token.token_type;
  await fs.writeFile(tokenPath, JSON.stringify(token, null, 2));
  return token.access_token;
}

function metadata() {
  return {
    snippet: {
      title: "SwarmOps Case Commander: Governed Agent Swarms for Enterprise Case Work",
      description: [
        "SwarmOps Case Commander is a UiPath AgentHack project for governed enterprise case work.",
        "The demo shows a vendor onboarding and rush purchase approval flow where bounded agents produce scoped analysis, risky vendor setup pauses for human approval, and the final state becomes audit-ready evidence.",
        "Hosted submission page: https://d0ubl3-a.github.io/swarmops-case-commander/",
        "Public repo: https://github.com/D0ubl3-A/swarmops-case-commander",
        "Versioned release: https://github.com/D0ubl3-A/swarmops-case-commander/releases/tag/v0.1.0",
        "Submission bundle: https://github.com/D0ubl3-A/swarmops-case-commander/releases/download/v0.1.0/swarmops-case-commander-submission-bundle.zip",
        "Deck: https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/artifacts/swarmops-case-commander-deck.pdf",
        "OpenAPI contract: https://raw.githubusercontent.com/D0ubl3-A/swarmops-case-commander/main/docs/openapi.json",
        "Important: the local prototype, handoff API, evidence pipeline, deck, and narrated video artifact are implemented and verified. UiPath Maestro Case is the target orchestration layer; full UiPath integration should be claimed only after Automation Cloud / Maestro footage is recorded.",
      ].join("\n\n"),
      categoryId: "28",
      tags: [
        "UiPath",
        "AgentHack",
        "Maestro Case",
        "AI agents",
        "enterprise automation",
        "agent governance",
        "human in the loop",
        "audit trail",
        "procurement automation",
        "case management",
        "responsible AI",
        "workflow automation",
        "OpenAPI",
        "Python",
        "JavaScript",
      ],
    },
    status: {
      privacyStatus: process.env.YOUTUBE_PRIVACY_STATUS || "unlisted",
      selfDeclaredMadeForKids: false,
      embeddable: true,
      publicStatsViewable: false,
      containsSyntheticMedia: false,
    },
  };
}

async function upload(accessToken) {
  const stat = await fs.stat(videoPath);
  if (!stat.isFile() || stat.size <= 0) throw new Error(`${videoPath} is not a readable video file.`);

  const initResponse = await fetch("https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${accessToken}`,
      "Content-Type": "application/json; charset=UTF-8",
      "X-Upload-Content-Type": "video/mp4",
      "X-Upload-Content-Length": String(stat.size),
    },
    body: JSON.stringify(metadata()),
  });
  if (!initResponse.ok) await parseJsonResponse(initResponse, "YouTube upload init");

  const uploadUrl = initResponse.headers.get("location");
  if (!uploadUrl) throw new Error("YouTube upload init did not return a resumable upload URL.");

  const uploadResponse = await fetch(uploadUrl, {
    method: "PUT",
    headers: {
      "Content-Type": "video/mp4",
      "Content-Length": String(stat.size),
    },
    body: createReadStream(videoPath),
    duplex: "half",
  });
  const payload = await parseJsonResponse(uploadResponse, "YouTube video upload");
  if (!payload.id) throw new Error("YouTube upload completed without a video id.");
  return String(payload.id);
}

async function verify(accessToken, videoId) {
  const url = new URL("https://www.googleapis.com/youtube/v3/videos");
  url.searchParams.set("part", "snippet,status");
  url.searchParams.set("id", videoId);
  const response = await fetch(url, { headers: { Authorization: `Bearer ${accessToken}` } });
  const payload = await parseJsonResponse(response, "YouTube upload verify");
  const video = payload.items?.[0];
  if (!video?.id) throw new Error(`YouTube did not return uploaded video ${videoId}.`);
  if (video.status?.privacyStatus !== (process.env.YOUTUBE_PRIVACY_STATUS || "unlisted")) {
    throw new Error(`YouTube video privacy is ${video.status?.privacyStatus || "unknown"}.`);
  }
  if (video.status?.embeddable !== true) throw new Error("YouTube video is not embeddable.");
  if (["deleted", "failed", "rejected"].includes(video.status?.uploadStatus)) {
    throw new Error(`YouTube upload status is ${video.status.uploadStatus}.`);
  }
  return video;
}

async function main() {
  await fs.access(metadataPath);
  const accessToken = await getAccessToken();
  const videoId = await upload(accessToken);
  const video = await verify(accessToken, videoId);
  const result = {
    uploadedAt: new Date().toISOString(),
    youtubeVideoId: videoId,
    youtubeUrl: `https://www.youtube.com/watch?v=${videoId}`,
    embedUrl: `https://www.youtube.com/embed/${videoId}`,
    privacyStatus: video.status?.privacyStatus || null,
    embeddable: video.status?.embeddable ?? null,
    uploadStatus: video.status?.uploadStatus || null,
    title: video.snippet?.title || null,
  };
  await fs.writeFile(outputPath, JSON.stringify(result, null, 2));
  console.log(JSON.stringify({ event: "swarmops-youtube-uploaded", youtubeUrl: result.youtubeUrl }, null, 2));
}

main().catch((error) => {
  console.error(JSON.stringify({ event: "swarmops-youtube-upload-failed", error: redact(error?.message || error) }));
  process.exitCode = 1;
});

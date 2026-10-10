from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 168.83,
    "uptime_pct": 98.265,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 183.1,
    "uptime_pct": 97.842,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 118.57,
    "uptime_pct": 98.234,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 218.14,
    "uptime_pct": 97.62,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 172.96,
    "uptime_pct": 99,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 111.41,
    "uptime_pct": 97.164,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 190.62,
    "uptime_pct": 97.138,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 211.92,
    "uptime_pct": 97.366,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 223.68,
    "uptime_pct": 97.961,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 157.65,
    "uptime_pct": 98.975,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 175.3,
    "uptime_pct": 97.186,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 134.9,
    "uptime_pct": 97.649,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 151.11,
    "uptime_pct": 99.213,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 147.89,
    "uptime_pct": 99.409,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 220.21,
    "uptime_pct": 98.15,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 232.69,
    "uptime_pct": 99.029,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 172.18,
    "uptime_pct": 98.239,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 221.08,
    "uptime_pct": 97.495,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 112.98,
    "uptime_pct": 97.72,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 133.6,
    "uptime_pct": 97.886,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 224.87,
    "uptime_pct": 99.399,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 167.4,
    "uptime_pct": 98.784,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 194.17,
    "uptime_pct": 99.486,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 167.09,
    "uptime_pct": 98.224,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 174.79,
    "uptime_pct": 99.446,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 118.32,
    "uptime_pct": 99.15,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 227.99,
    "uptime_pct": 98.159,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 167.87,
    "uptime_pct": 98.463,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 224.14,
    "uptime_pct": 97.644,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 220.25,
    "uptime_pct": 99.322,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 145.88,
    "uptime_pct": 97.371,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 145.95,
    "uptime_pct": 98.312,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 165.89,
    "uptime_pct": 98.379,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 185.33,
    "uptime_pct": 97.384,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 120.11,
    "uptime_pct": 98.549,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 221.97,
    "uptime_pct": 97.968,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}

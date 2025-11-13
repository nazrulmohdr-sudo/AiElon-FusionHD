import axios from 'axios';
import dotenv from 'dotenv';
dotenv.config();

// UNIVERSAL BRAIN ROUTER
export async function AiElonBrain(query) {
  const engines = [
    { name: "ChatGPT",  url: process.env.OPENAI_API },
    { name: "Claude",   url: process.env.CLAUDE_API },
    { name: "DeepSeek", url: process.env.DEEPSEEK_API },
    { name: "Grok",     url: process.env.GROK_API },
    { name: "Meta",     url: process.env.META_API },
    { name: "Gemini",   url: process.env.GEMINI_API }
  ];

  let results = [];
  for (const e of engines) {
    try {
      if (!e.url) {
        results.push({ engine: e.name, response: "NOT CONFIGURED" });
        continue;
      }
      const res = await axios.post(e.url, { prompt: query });
      results.push({ engine: e.name, response: res.data });
    } catch (error) {
      results.push({ engine: e.name, response: "OFFLINE / SKIP", error: error.message });
    }
  }

  return {
    query,
    summary: "Unified AiElon Intelligence Response",
    results
  };
}

// CLI usage example
if (import.meta.url === `file://${process.argv[1]}`) {
  const testQuery = process.argv[2] || "Hello from AiElon Brain!";
  console.log("🧠 AIELON BRAIN - Processing query...");
  console.log("Query:", testQuery);
  
  AiElonBrain(testQuery)
    .then(response => {
      console.log("\n✅ Results:");
      console.log(JSON.stringify(response, null, 2));
    })
    .catch(error => {
      console.error("❌ Error:", error.message);
    });
}

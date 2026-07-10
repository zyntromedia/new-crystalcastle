// hooks/useAIStream.ts
import { useState } from "react";

export function useAIStream() {
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);

  async function sendPrompt(prompt: string) {
    setOutput("");
    setLoading(true);

    const response = await fetch("/api/ai", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });

    const reader = response.body?.getReader();
    const decoder = new TextDecoder();

    if (!reader) {
      setLoading(false);
      return;
    }

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      setOutput((prev) => prev + decoder.decode(value));
    }

    setLoading(false);
  }

  return { output, loading, sendPrompt };
}

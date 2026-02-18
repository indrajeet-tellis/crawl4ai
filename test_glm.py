import os
import litellm
from litellm import completion

# ZAI Anthropic-compatible configuration
ZAI_API_KEY = "4b49e782ab9e4e4aa709b3670165007e.jypz3UD9bxOaPPQR"
ANTHROPIC_BASE_URL = "https://api.z.ai/api/anthropic"
MODEL = "anthropic/glm-4.7"

def test_glm():
    print(f"Testing model: {MODEL}")
    print(f"Base URL: {ANTHROPIC_BASE_URL}")
    
    try:
        response = completion(
            model=MODEL,
            messages=[{"role": "user", "content": "Hello, how are you?"}],
            api_key=ZAI_API_KEY,
            base_url=ANTHROPIC_BASE_URL,
            temperature=0.7
        )
        print("\n--- Response ---")
        print(response.choices[0].message.content)
        print("--- End ---")
        return True
    except Exception as e:
        print(f"\nError: {e}")
        return False

if __name__ == "__main__":
    test_glm()

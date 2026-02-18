import requests
import json
import time

CRAWL4AI_URL = "http://localhost:11235/md"
TEST_URL = "https://example.com"

def verify_glm_extraction():
    print(f"Testing GLM extraction via {CRAWL4AI_URL}")
    print(f"Target URL: {TEST_URL}")
    
    payload = {
        "url": TEST_URL,
        "f": "llm",
        "q": "What is the title of this page? Respond in JSON format with a 'title' key.",
        "c": str(int(time.time()))
    }
    
    try:
        response = requests.post(CRAWL4AI_URL, json=payload, timeout=60)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("\n--- Extraction Result ---")
            print(result.get("markdown", "No markdown returned"))
            print("--- End ---")
            
            if result.get("success"):
                print("✅ GLM Extraction Succeeded!")
                return True
            else:
                print("❌ Extraction reported failure.")
                return False
        else:
            print(f"❌ Request failed: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error during request: {e}")
        return False

if __name__ == "__main__":
    # Wait a bit for the server to be fully ready if called immediately after docker-compose up
    # print("Waiting for server to be ready...")
    # time.sleep(5) 
    verify_glm_extraction()

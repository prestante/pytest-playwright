import yaml
import json

if __name__ == "__main__":
    with open("/Users/pres/PY/pytest-playwright/.github/workflows/playwright.yml") as f:
        templates = yaml.safe_load(f)
    
    #print(templates)
    print(json.dumps(templates, indent=4))


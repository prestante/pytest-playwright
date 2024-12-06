import yaml
import json

if __name__ == "__main__":
    with open("./test.yaml") as f:
        templates = yaml.safe_load(f)
    
    #print(templates)
    print(json.dumps(templates, indent=4))


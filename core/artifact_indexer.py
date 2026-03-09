import os

class ArtifactIndexer:

    def __init__(self, artifact_root="artifacts"):
        self.artifact_root = artifact_root

    def index(self):

        artifacts = []

        for browser in os.listdir(self.artifact_root):

            browser_path = os.path.join(self.artifact_root, browser)

            if not os.path.isdir(browser_path):
                continue

            for root, dirs, files in os.walk(browser_path):

                for file in files:
                    
                    artifacts.append({
                        "browser": browser,
                        "path": os.path.join(root, file),
                        "file": file,
                        "type": file.split(".")[-1],
                        "test": file.split("_")[0]
                    })

        return artifacts
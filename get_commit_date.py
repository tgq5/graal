import json
from pydriller import Git, Repository
from utils.utils import match_bics, remove_empty_bug_hashs, update_matched_v2
import sys
import os
from datetime import timedelta

def get_commit_date(json_file, repo):
    with open(json_file) as f:
        data = json.load(f)
        for d in data:
           commit_hash = d["fix_commit_hash"]
           for commit in Repository(repo, single=commit_hash).traverse_commits():
                new_date = commit.author_date + timedelta(seconds=60)
                d["best_scenario_issue_date"] = new_date.isoformat()  # Salva como string em ISO 8601

    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

for file in os.listdir("./json/raw_data"):
    json_file = f"./json/raw_data/{file}"
    get_commit_date(json_file, f"repos_dir/graal")

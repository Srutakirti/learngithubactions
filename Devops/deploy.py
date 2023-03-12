import pathlib

# p = pathlib.Path(__file__)


# x = pathlib.Path("databricks_notebook_jobs\data_validations")

# print(x)

# for k in x.iterdir():
#     print(k)

def get_changed_jobs(diff_file):
    with open(diff_file,"r", errors='ignore') as f:
        print(f.readlines())


def process_diff(diff_file):
    job_json_dict = {}
    with open(diff_file,"r", errors='ignore') as f:
        for folder in f.readlines():
            folder_path = pathlib.Path(folder)
            job_json_dict[folder] = list(folder_path.glob("*.json"))
    return job_json_dict

output = get_changed_jobs("diff.txt")

print(output)



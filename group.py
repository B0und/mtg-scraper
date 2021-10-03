import glob

result_list = []

for txt_path in glob.glob("./txt_folder/*.txt"):
    with open(txt_path) as f:
        content = [line.rstrip() for line in f]
        result_list += content

# get rid of duplicates
result_list = list(set(result_list))
with open("FINAL_FINAL.txt", "w") as fout:
    print(*result_list, sep="\n", file=fout)

## 2. Extract Line Numbers ##

raw_hamlet = sc.textFile("hamlet.txt")
split_hamlet = raw_hamlet.map(lambda line: line.split('\t'))
split_hamlet.take(5)

def format_id(x):
    id = x[0].split('@')[1]
    results = list()
    results.append(id)
    if len(x) > 1:
        for y in x[1:]:
            results.append(y)
    return results

hamlet_with_ids = split_hamlet.map(lambda line: format_id(line))
hamlet_with_ids.take(10)

## 3. Remove Blank Values ##

hamlet_with_ids.take(5)
text = hamlet_with_ids.filter(lambda line: len(line)>1)
hamlet_text_only = text.map(lambda line: [i for i in line if i != ""])
hamlet_text_only.take(5)

## 4. Remove Pipe Characters ##

hamlet_text_only.take(10)
# clean_hamlet = hamlet_text_only.map(lambda line: [i.replace("|",'') if "|" in i  else i for i in line])
# clean_hamlet.take(5)

def fix_pipe(line):
    results = list()
    for l in line:
        if l == "|":
            pass
        elif "|" in l:
            fmtd = l.replace("|", "")
            results.append(fmtd)
        else:
            results.append(l)
    return results

clean_hamlet = hamlet_text_only.map(lambda line: fix_pipe(line))
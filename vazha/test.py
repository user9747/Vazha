import re
import keyword



# from googletrans import Translator
# translator = Translator()


# translations = translator.translate(l, dest='ml')
# for translation in translations:
#     print(translation.text,'=',translation.origin) 


# import json
# with open('vazha_to_manglish.json') as f:
#     a = json.load(f)
#     d = a["keywords"]
#     for i in d:
#         name = d[i].replace(" ","")
#         print("const {}Completion = new vscode.CompletionItem('{}');".format(name,i))
#         print("{}Completion.filterText = '{}';".format(name,d[i]))
#         print("{}Completion.kind = vscode.CompletionItemKind.Keyword;".format(name))
#         print("completion_items.push({}Completion)".format(name))
#         print()

# from googletrans import Translator
# translator = Translator()


# keywords = []
# for k in keyword.kwlist:
#     if(k not in __builtins__.__dict__):
#         keywords.append(k)
# print(keywords)

# translations = translator.translate(keywords, dest='ml')
# for translation in translations:
#     print(translation.text,'=',translation.origin) 

s=""
import json
with open('vazha_to_eng.json') as f:
    a = json.load(f)
    d = a["built_ins"]
    for i in d:
        s=s+"|"+i



print(s)
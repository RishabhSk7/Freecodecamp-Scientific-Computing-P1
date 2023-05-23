def arithmetic_arranger(problems,  out=False):
  try:
    if len(problems)>5:
        raise Exception("Too many problems.")
    problems = [x.split(" ") for x in problems]
    
    if False in list(map(lambda x: True if x[1] in ("+", "-") else False, problems)):
        raise Exception("Operator must be '+' or '-'.")

    if False in list(map(lambda x: True if (x[0].isdigit() and x[-1].isdigit()) else False, problems)):
        raise Exception("Numbers must only contain digits.")

    if False in list(map(lambda x: True if (len(x[0])<5 and len(x[-1])<5) else False, problems)):
        raise Exception("Numbers must only contain digits.")

    opr1s_list = []
    opr2s_list = []
    dashes = []
    output=[]
    for i in problems:
        lenght = max(len(i[0]), len(i[2]))

        if lenght == len(i[0]):
           operand1 = " "*2+i[0]
           operand2 = i[1]+" "+" "*(lenght-len(i[2]))+i[2]
        else:
           operand1 = " "*2+" "*(lenght-len(i[0]))+i[0]
           operand2 = i[1]+" "+i[2]
        
        if out:
           result = str(eval(" ".join(i)))
           output.append(" "*(lenght+2-len(result))+result)
        
        dashes.append("-"*(lenght+2))
        opr1s_list.append(operand1)
        opr2s_list.append(operand2)

    
    return '    '.join(opr1s_list)+"\n"+'    '.join(opr2s_list)+"\n"+'    '.join(dashes)+"\n"+'    '.join(output)

  except Exception as E:
    return "Error: "+E.args[0]


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
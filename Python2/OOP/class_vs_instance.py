class emp:
    language="python"#class attributes
    salary=12000
new=emp()
new.language="CSharp"#instance attribute
print(new.language,new.salary)

#  output is CSharp 12000
# because in python instance attribute is given more 
# preference than class attribute
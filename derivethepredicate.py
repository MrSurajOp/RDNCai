def implies(A, B):
    return (not A) or B

def double_implies(A, B):
    return (A and B) or (not A and not B)

def evaluate_logic(A, B):
    sentence_A = "It is raining."
    sentence_B = "The ground is wet."
    
    and_result = A and B
    or_result = A or B
    not_A_result = not A
    implies_result = implies(A, B)
    double_implies_result = double_implies(A, B)
    
    print(f"{sentence_A} AND {sentence_B}:")
    if and_result:
        print(f"Both statements are true: 'It is raining' and 'The ground is wet.'\n")
    else:
        print(f"At least one statement is false: 'It is raining' and 'The ground is wet.'\n")
    
    print(f"{sentence_A} OR {sentence_B}:")
    if or_result:
        print(f"At least one of the statements is true: 'It is raining' or 'The ground is wet.'\n")
    else:
        print(f"Both statements are false: 'It is not raining' and 'The ground is not wet.'\n")
    
    print(f"NOT ({sentence_A}):")
    if not_A_result:
        print(f"'It is not raining.'\n")
    else:
        print(f"'It is raining.'\n")
    
    print(f"({sentence_A}) IMPLIES ({sentence_B}):")
    if implies_result:
        print(f"If 'It is raining', then 'The ground is wet' is true.\n")
    else:
        print(f"The statement 'If it is raining, then the ground is wet' is false.\n")
    
    print(f"({sentence_A}) IF AND ONLY IF ({sentence_B}):")
    if double_implies_result:
        print(f"'It is raining' if and only if 'The ground is wet' (both are either true or false).\n")
    else:
        print(f"'It is raining' does not correspond to 'The ground is wet' (one is true and the other is false).\n")

A = True  # It is raining.
B = False  # The ground is not wet.
evaluate_logic(A, B)

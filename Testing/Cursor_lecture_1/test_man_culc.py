

import culc

def test_add():
    if culc.add(2, 3) == 5:
        print("True")
    else:
        print("False")

def test_red():
    if culc.red(4, 3) == 1:
        print("True")
    else:
        print("False")

def test_mult():
    if culc.mult(2, 3) == 6:
        print("True")
    else:
        print("False")

def test_div():
    if culc.div(12, 3) == 4:
        print("True")
    else:
        print("False")

test_add()
test_red()
test_mult()
test_div()
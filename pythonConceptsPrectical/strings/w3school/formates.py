txt = "We have {:<8} Apples." #use < left-align
txt = "We have {:>8} Apples." #use > right-align
txt = "We have {:^8} Apples." #use ^ center-align
txt = "The Temperature is {:=8} degrees celsuius." #use = plus/minus sign at the left most position
txt = "The Temperature is between {:+} and {:+} degrees celsuius."
txt = "The Temperature is between {:-} and {:-} degrees celsuius."
txt = "The universe is {:,} years old"
txt = "The universe is {:_} years old"
txt = "The binary version of {0} is {0:b}" #convert d to b
txt = "We have {:d} Apples." #convert b to d
txt = "We have {:e} Apples." #convert d to scientific
txt = "We have {:E} Apples."
txt = "We have {:.2f} Apples."
txt = "We have {:f} Apples."
txt = "We have {0} Apples. {0:o}" #convert d to o

print(txt.format(10))
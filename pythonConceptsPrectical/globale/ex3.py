def outer():
    messaage = 'local'

    def inner():
        nonlocal messaage  # <<<<<<<<<<<<<<

        messaage = 'nonlocal'
        print("inner : ",messaage)

    inner()
    print("outer",messaage)

outer()
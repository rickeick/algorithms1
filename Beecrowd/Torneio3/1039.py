while True:
    try:
        Rc, Xc, Yc, Rf, Xf, Yf = map(int, input().split())
        D = ((Xf - Xc)**2 + (Yf - Yc)**2)**0.5
        if Rc >= D + Rf: print('RICO')
        else: print('MORTO')
    except EOFError: break

print('sum3(2)(4)(6) =', (lambda x: (lambda y: (lambda z: (x + y + z))))(2)(4)(6))

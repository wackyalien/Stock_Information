import insertion,algo,sys
print 'x'*20,'Welcome in my project','x'*20
print 'Wanna enter new data'
data= raw_input('Y/N?')
if data == 'Y':
    insertion.insert()
    print 'Thank you..Visit again!!'
elif data == 'N':
    print 'wanna send mail to your Client'
    data1 = raw_input('Y/N?')
    if data1 == 'Y':
        algo.algorithm()
        print 'Thank you..Visit again!!'
    elif data1 == 'N':
        print 'Thank you to visit'
    else:
        print 'wrong input...Please visit again!!'
        sys.exit(1)
else:
    print 'wrong input...Please visit again!!'
    sys.exit(1)

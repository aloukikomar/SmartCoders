
import time
from TestCases.CrBase import mainCr
from TestCases.Functional import mainFn
from TestCases.SmokeBasic import mainSmBS
from TestCases.SmokeComplex import mainSmCo
from TestCases.ApiBased import mainApiCart
#------|Main Automation Flow file ---------------------------------#


def myFlow():
    Result = {}
    FCount=0
    PCount=0
    TimeStamp = str(int(time.time()))
    #------|make log#
    open("Log/Automation_{}.txt".format(TimeStamp),"w+").write("====Automation Test {}==================================================================\n".format(TimeStamp))
    print("====Automation Test {}==================================================================\n".format(TimeStamp))
    fileob=open("Log/Automation_{}.txt".format(TimeStamp),"a+")
    
    
    #------|start test case#
    fileob.write("Starting Test Case 1 \n")
    print("Starting Test Case 1 \n")


    ##################################################
    # Critical |  Site up and working
    ##################################################

    #------| Test Hompage is up  #

    TestFlag1=mainCr()
    if TestFlag1 == 1:
        Result['Test1']="PASS"
        PCount=PCount+1
    else:
        Result['Test1']="FAIL"
        FCount=FCount+1
        print ("Critical Test Case Failed | Site is Down")
        return 0

    fileob.write("Completed Test Case 1 | Result {}\n".format(Result['Test1']))
    print ("Completed Test Case 1 | Result {}\n".format(Result['Test1']))
    #------| End test Casse#
         
    #------|start test case#
    fileob.write("Starting Test Case 2 \n")
    print("Starting Test Case 2 \n")
    #------| Test case for smoke test of add to cart feature from UI #
    TestFlag2=mainFn()
    if TestFlag2 == 1:
        Result['Test2']="PASS"
        PCount=PCount+1
    else:
        Result['Test2']="FAIL"
        FCount=FCount+1
    fileob.write("Completed Test Case 2 | Result {}\n".format(Result['Test2']))
    print ("Completed Test Case 2 | Result {}\n".format(Result['Test2']))
    #------| End test Casse#


    #------|start test case#
    fileob.write("Starting Test Case 3 \n")
    print("Starting Test Case 3 \n")
    #------| Test case to check integration of add to cart feature from UI #
    TestFlag3=mainSmBS()
    if TestFlag3 == 1:
        Result['Test3']="PASS"
        PCount=PCount+1
    else:
        Result['Test3']="FAIL"
        FCount=FCount+1
    fileob.write("Completed Test Case 3 | Result {}\n".format(Result['Test3']))
    print("Completed Test Case 3 | Result {}\n".format(Result['Test3']))
    #------| End test Casse#


    #------|start test case#
    fileob.write("Starting Test Case 4 \n")
    print("Starting Test Case 4 \n")
    #------| Test case to check integration of add to cart feature from UI with more than one user #
    TestFlag4=mainSmCo()
    if TestFlag4 == 1:
        Result['Test4']="PASS"
        PCount=PCount+1
    else:
        Result['Test4']="FAIL"
        FCount=FCount+1
    fileob.write("Completed Test Case 4 | Result {}\n".format(Result['Test4']))
    print("Completed Test Case 4 | Result {}\n".format(Result['Test4']))
    #------| End test Casse#


    #------|start test case#
    fileob.write("Starting Test Case 5 \n")
    print("Starting Test Case 5 \n")
    #------| Test case to check integration of add to cart feature from Api #
    TestFlag5=mainApiCart()
    if TestFlag5 == 1:
        Result['Test5']="PASS"
        PCount=PCount+1
    else:
        Result['Test5']="FAIL"
        FCount=FCount+1
    fileob.write("Completed Test Case 5 | Result {}\n".format(Result['Test4']))
    print("Completed Test Case 5 | Result {}\n".format(Result['Test4']))
    #------| End test Casse#


    fileob.close()

    #------| check Failure #
    if FCount > 0:
        open("Log/Automation_{}.txt".format(TimeStamp),"a+").write("====Status : Fail ==================================================================\n{}\n".format(Result))
        print("====Status : Fail ==================================================================\n{}\n".format(Result))
    else:
        open("Log/Automation_{}.txt".format(TimeStamp),"a+").write("====Status : Pass ==================================================================\n{}\n".format(Result))
        print("====Status : Pass ==================================================================\n{}\n".format(Result))
    
    #------| End Result#
    open("Log/Automation_{}.txt".format(TimeStamp),"a+").write("Total Test Cases :{} Pass : {} Fail : {}\n".format(PCount+FCount,PCount,FCount))
    print("Total Test Cases :{} Pass : {} Fail : {}\n".format(PCount+FCount,PCount,FCount))




#------| Run Automation#
myFlow()
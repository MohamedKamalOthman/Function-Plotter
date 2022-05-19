from main import*
#our test object
testObject = main()

#our test functions
def testEmpty():
    assert testObject.expression == "", "Should be empty string"
    print("Test 1 Passed")
    
def testErrors():
    assert testObject.update_graph() == None, "Should be None"
    testObject.expression = "sin(x)ghf"
    assert testObject.update_graph() == None, "Shouldn't be None"
    testObject.expression = "1+^*x"
    assert testObject.update_graph() == None, "Shouldn't be None"
    print("Test 2 Passed")
    
def testSin():
    testObject.expression = "sin(x)"
    plot, = testObject.update_graph()
    x = np.arange(testObject.min, testObject.max, 0.1)
    np.testing.assert_array_equal(plot.get_ydata(), np.sin(x))
    print("Test 3 Passed")

def testSinh():
    testObject.expression = "sinh(x)"
    plot, = testObject.update_graph()
    x = np.arange(testObject.min, testObject.max, 0.1)
    np.testing.assert_array_equal(plot.get_ydata(), np.sinh(x))
    print("Test 4 Passed")
    
def testCos():
    testObject.expression = "cos(x)"
    plot, = testObject.update_graph()
    x = np.arange(testObject.min, testObject.max, 0.1)
    np.testing.assert_array_equal(plot.get_ydata(), np.cos(x))
    print("Test 5 Passed")  
    
def testCosh():
    testObject.expression = "cosh(x)"
    plot, = testObject.update_graph()
    x = np.arange(testObject.min, testObject.max, 0.1)
    np.testing.assert_array_equal(plot.get_ydata(), np.cosh(x))
    print("Test 6 Passed")   
    
def testTan():
    testObject.expression = "tan(x)"
    plot, = testObject.update_graph()
    x = np.arange(testObject.min, testObject.max, 0.1)
    np.testing.assert_array_equal(plot.get_ydata(), np.tan(x))
    print("Test 7 Passed") 
    
def testTanh():
    testObject.expression = "tanh(x)"
    plot, = testObject.update_graph()
    x = np.arange(testObject.min, testObject.max, 0.1)
    np.testing.assert_array_equal(plot.get_ydata(), np.tanh(x))    
    print("Test 8 Passed")   
    
def testAbs():
    testObject.expression = "abs(x)"
    plot, = testObject.update_graph()
    x = np.arange(testObject.min, testObject.max, 0.1)
    np.testing.assert_array_equal(plot.get_ydata(), np.abs(x))   
    print("Test 9 Passed")
    
def testLn():
    testObject.expression = "ln(x)"
    plot, = testObject.update_graph()
    x = np.arange(testObject.min, testObject.max, 0.1)
    np.testing.assert_array_equal(plot.get_ydata(), np.log(x))  
    print("Test 10 Passed")
    
def testLog():
    testObject.expression = "log(x)"
    plot, = testObject.update_graph()
    x = np.arange(testObject.min, testObject.max, 0.1)
    np.testing.assert_array_equal(plot.get_ydata(), np.log10(x))   
    print("Test 11 Passed")
    
def testSqrt():
    testObject.expression = "sqrt(x)"
    plot, = testObject.update_graph()
    x = np.arange(testObject.min, testObject.max, 0.1)
    np.testing.assert_array_equal(plot.get_ydata(), np.sqrt(x))   
    print("Test 12 Passed")
    
def testPolynomail():
    testObject.expression = "5*x**3 + 2*x"
    plot, = testObject.update_graph()
    x = np.arange(testObject.min, testObject.max, 0.1)
    np.testing.assert_array_equal(plot.get_ydata(), 5*x**3+2*x) 
    print("Test 13 Passed")
    
def testAll():
    testObject.expression = "sin(x+pi/e+cos(tan(x**2)))"
    plot, = testObject.update_graph()
    x = np.arange(testObject.min, testObject.max, 0.1)
    np.testing.assert_array_equal(plot.get_ydata(),np.sin(x+np.pi/np.e+np.cos(np.tan(x**2))))
    print("Test 14 Passed")
    
#our main function
if __name__ == "__main__":
    testObject.min = -10
    testObject.max = 10
    testEmpty()
    testErrors()
    testSin()
    testSinh()
    testCos()
    testCosh()
    testTanh()
    testTan()
    testAbs()
    testLn()
    testLog()
    testSqrt()
    testPolynomail()
    testAll()
    print("Passed All Tests")
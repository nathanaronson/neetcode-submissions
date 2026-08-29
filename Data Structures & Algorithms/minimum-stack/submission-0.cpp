class MinStack {
    stack<int> minSt, mainSt;
public:
    MinStack() {}
    
    void push(int val) {
        mainSt.push(val);
        val = min(val, minSt.empty() ? val : minSt.top());
        minSt.push(val);
    }
    
    void pop() {
        minSt.pop();
        mainSt.pop();
    }
    
    int top() {
        return mainSt.top();
    }
    
    int getMin() {
        return minSt.top();
    }
};

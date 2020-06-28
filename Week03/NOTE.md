## 3rd week 学习笔记

### 1 递归的[Python代码模板](https://shimo.im/docs/EICAr9lRPUIPHxsH/read)
```
def recursion(level, param1, param2, ...):
    # recursion terminator (Part1 递归终止条件)
    if level > MAX_LEVEL:
        process_result
        return
    
    # process logic in current level （Part2 处理当前逻辑）
    process(level, data...)

    # drill down （Part3 下探到下一层）
    selft.recursion(level + 1, p1, ...)

    # reverse the current level status if needed （Part4 清理当前层）

```
### 2 [分治代码模板](https://shimo.im/docs/zvlDqLLMFvcAF79A/read)
```
def divide_conquer(problem, param1, param2, ...):
    # recursion terminator
    if problem is None:
        print_result
        return
    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)
    # conquer subproblems
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)
    …
    # process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, …)

    # revert the current level states
```

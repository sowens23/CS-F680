# CS-F680 Deep Learning With Python
## Class Notes and Homework Repository :dizzy: :earth_americas:
  ```
  #include <iostream>
  int main() {
    std::cout << "Hello traveller, here's a towel for protection. Take care of yourself out there." << std::endl;
    return 0;
  }
  ```
  ![Hitchhikers Guide to the Galaxy](https://github.com/sowens23/CS-F311/blob/main/inclasscoding/week1/tenor.gif)

### Class Repositories and References
  - [sowens23-GitHub](https://github.com/sowens23)
  - [GitHubPortal](https://github.com/sowens23/Newbie-Gains/blob/main/README.md)

### Big Notes
  - 

# Class Notes and Assignments
# CS-F331 Computer Languages
## Class Notes and Homework Repository :dizzy: :earth_americas:
  ```
  #include <iostream>
  int main() {
    std::cout << "Hello traveller, here's a towel for protection. Take care of yourself out there." << std::endl;
    return 0;
  }
  ```
  ![Hitchhikers Guide to the Galaxy](https://github.com/sowens23/CS-F311/blob/main/inclasscoding/week1/tenor.gif)

### Class Repositories and References
  - [sowens23-GitHub](https://github.com/sowens23)
  - [GitHubPortal](https://github.com/sowens23/Newbie-Gains/blob/main/README.md)
  - [CS-F680 Class Homepage](https://canvas.alaska.edu/courses/20866)

### Big Notes
  - Focus here is to learn Python, NumPy, and TensorFlow

# Class Notes and Assignments
  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  | [Week-1](#Week-1) | [Week-2](#Week-2) | [Week-3](#Week-3) | [Week-4](#Week-4) | [Week-5](#Week-5) | 
  | [Week-6](#Week-6) | [Week-7](#Week-7) | [Week-8](#Week-8) | [Week-9](#Week-9) | [Week-10](#Week-10) | 
  | [Week-11](#Week-11) | [Week-12](#Week-12) | [Week-13](#Week-13) | [Week-14](#Week-14) | [Week-15](#Week-15) | 

# Week-1
[Top](#TOP)
## 2024-09-03
  ### Python Programming and Using Libraries
  - First dimensional data structure is an List, second dimensional data structure is an Array, third is a Matrix, and fourth and past is a Tensor. Hense, TensorFlow
  - We can convert Array/Matrix/Tensor into NumPy array. We can do this using the np.array({LIST}) function.
  - NumPy can only handle numbers. No handling strings, etc in NumPy lists.
  - Using NumPu lists, we can use a range of arithmetic operations.
  - Let's look at a 2-D Array
    ```py
    arr1_2d = np.array ([
      [1, 2, 3],
      [4, 5, 6]
    ])
    
    arr2_2d = np.array ([
      [6, 5, 4],
      [3, 2, 1]
    ])

    result = arr1_2d + arr2_2d
    print(result)
    ``` 
  - The reason we use NumPy is because it is faster when manipulating and handling large amount of numerical data, compared to Python lists.
  
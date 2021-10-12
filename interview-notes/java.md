---
title: Java Fundamentals
---

## Association
Association is a relationship between objects. Aggregation and composition are types of association.

### Aggregation
Aggregation is a kind of HAS-A relationship between objects. One object takes ownership of the other. However, both can exist independently. For example, In a chessboard - box and color.

### Composition
Composition is a kind of strong aggregation between objects and the child object can't exist in the absence of the parent. For example, In a chessboard, Board and Box

## Difference between String initialization using = operator and new operator

If the String variable is initialized using an assignment operator, it will be placed in the String pool and a reference to the string pool entry will be returned.

If the String variable is initialized using the new operator, it will be created in the heap area - outside the string pool.

synchronising a method.

```
public class Counting {
       private int increase_counter;
       public synchronized int increase() {
               increase_counter = increase_counter + 1;
               return increase_counter;
       }
}
```

## varargs (...)
```
void String concatStrs(String... strings) {
  // logic
}
```

The above method can take multiple arguments.

## Lifecycle of Java thread

1. New - The tread is created using the new keyword, but not started yet.
2. Runnable - Thread is started, but the run method is not called yet.
3. Running - run method is called, and running is in progress.
4. Waiting - Asked to wait() during the execution, and waiting for a signal to execute from any other thread.
5. Blocked - Waiting for some synchronized code execution.
6. Terminated - Completed the execution of the run method.

![Thread lifecycle](/assets/images/post-images/spring-tutorial/java_thread_lifecycle.jpg)
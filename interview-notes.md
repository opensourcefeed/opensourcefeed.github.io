# Spring

## Spring Beans
- Objects manged by the Spring IoC container.
- Created as per the configuration metadata user provided to the container.

## Configuration metadata
- Describing the objects that need to instantiated and managed by the IOC container.
  - Pure XML
    <bean id="myBean" class="com.example.MyClass">
      <property name="prop" ref="secondBean"/>
    </bean>
  - Mention in the XML document to look for annotations
    <beans>
      <!-- Looks for the annotations inside beans which are already defined in the Xml file -->
      <context:annotation-config>
      <!-- Looks for the new bean definitions and annotations -->
      <context:component-scan base-package="org.example"/>
    </beans>
  - Pure annotation - @Configuration and @Bean annotations

## Spring Bean Scopes
- Singleton - In an IOC container
- Prototype
- Request
- Session
- Global Session

Note: Global Session will be coming into picture for portlet applications. In end-user point of view, portlet is a part of 
web page which receives request, gives response. There can be multiple portlets inside a web application. If we we want to share
beans across all these portlets, then we can use global session scoped beans

## Dependency Injection (DI)
In case of classess referring to other classess, there is no need for the developer to create the class objects. Instead, need to describe the objects, and which all objects will be having references to other objecs. The bean creation and giving the referred object will be done by the spring IoC contianer.

There are two ways of dependency injection - Setter & Constructor injection.
### Constructor Injection
- IoC container will invoke the class constructor with dependencies.
- Beans will be reinstantiated if any dependency modification happens.
- Partial initialization is not possible.

### Setter injection
- Calls the setter methods for the dependency injection after calling no-argment or default constructor
- Override the setter

## AOP
- Aspect - A module which offers some common functionalities which is separate from the business logic. Logging, authentication, ..etc
- Joint point - A place in the code where aspect can be introduced
- Advice - Actual piece of code that will be executed in join points
- Point cut - Set of one or more joint points where advice will be executed
- Introduction - Process of adding new methods or attributes
- Target object - Class with one or more aspects
- Weaving - Process of linking aspects with other application types or objects.

### AOP advices

- Before: executes before a join point, but it does not have the ability to prevent execution flow from proceeding to the join point (unless it throws an exception).
- AfterReturning: executed after a join point completes normally i.e if a method returns without throwing an exception.
- AfterThrowing: executed if a method exits by throwing an exception.
- After: executed regardless of the means by which a join point exits (normal return or exception encounter).
- Around:surrounds a join point such as a method invocation.


# Spring Boot
- Stand-alone JARS
- Embedded web server (tomcat), which are replaceable.
- Starter POMs
- Auto-configuration
- Spring actuators - management endpoints for going through the application internals.
- Logging and security

@SpringBootApplication
  - @Configuration
  - @EnableAutoConfiguration
  - @ComponentScan

@RestController
@RequestMapping

# Spring MVC
- Spring framework for web developement.
- Provides loose coupling between input logic (Model), business logic (Controller) and UI logic (View)

Dispatcher Servlet - Handles all Http Reqeusts and provides response
![Dispatcher Servlet Preview](/assets/images/post-images/spring-tutorial/DispatcherServlet_in_Spring_MVC.png)

- View Resolver will identify the view that is needed to render (Support HTML, JSP, JSF, XSLT ..etc).
- Defautl view resolve is InternalResourceViewResolver.
- ContextLoaderListener loads and creates the ApplicationContext, so a developer need not write explicit code to do create it
- @RequestParam and @PathVariable



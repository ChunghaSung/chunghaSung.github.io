---
layout: default
title: Research & Work Experience
---

<div class="post">

<h3>Modular verification of Interrupt-driven programs</h3>
<p> &nbsp; &nbsp;Since there has been relatively lack of verification 
methods for interrupt-driven programs even the behavior of interrupts is similar with that of threads, we introduced a more accurate verification 
method for interrupt-driven programs by leveraging a thread-modular 
analysis for concurrent programs. By modeling interrupt behavior such 
as priority information and preemption information with Z3 SMT solver, 
I combined this information with a thread-modular abstract interpretation 
analysis. Therefore, I could remove infeasible interference for interrupt-driven programs and could achieve a more accurate analysis without losing 
 computation overhead.<br>
&nbsp;&nbsp;
I compared our analysis to state-of-the-art techniques one of which is a thread-modular analysis for concurrent programs, and another is a model checking based interrupt-driven analysis tool, with about 35 C-base interrupt-driven programs. Finally, my tool showed its higher accuracy than other two tools with getting a little overhead.
<br>
&nbsp;&nbsp; Project link: <a href="https://github.com/chunghaSung/intabs">https://github.com/chunghaSung/intabs</a>
</p>

<h3>Extension of a Scope query optimization tool</h3>
<p>&nbsp;&nbsp;
During the internship at MSR, I extended a scope query optimization tool. The tool consists of two parts: one part is parser and another part is template generation. Basically, it parses a query file and then prints a C-style code template, and the template is fed into a programming synthesis tool to optimize it. Then, the optimized C-style program is translated into an optimized query. However, the tool only supported a small set of queries because many queries use many combinations of columns and uninterpreted functions. So, I changed more than half of the tool, both parser and template generation parts, to support various combinations of columns and uninterpreted functions. To achieve this, I got used to F#, C# and Scope query.
</p>

<h3>Optimization of testing web applications</h3>
<p>&nbsp;&nbsp;
Even though there were many approaches to analyze web applications, it was hard to analyze them accurately due to its inherent characteristic of user-driven events using the DOM (Document Object Model). This project tries to model the DOMs to find out dependencies between two events which are attached to the DOMs. To achieve this, I made a JavaScript parser from the scratch using JavaScript and nodejs, and modified JS_WALA to build a CFG (Control Flow Graph). Based on the CFG, translated datalog facts are printed. My analysis is inter-procedural and flow-insensitive pointer analysis. Finally, from the facts I got and the rules I made, I can figure out the dependencies among all events over-approximately.
<br>&nbsp;&nbsp;
To show the usefulness of my work, I hooked up the automated testing tool named Artemis to shrink the searching space of it using POR (Partial Order Reduction) with the dependency information. I tested with about 20 real world JavaScript games which are highly user-driven events demanded programs, and the result shows that the overhead of this analysis is really negligible and we got about 16% improvement of code coverage in average.
<br>&nbsp;&nbsp;
Project link: <a href="https://github.com/chunghaSung/jsdep">https://github.com/chunghaSung/jsdep</a>
</p>

<h3>Interactive Visualization</h3>
<p>&nbsp;&nbsp;
Our team developed an interactive visualization graphic package as an open source in R project during the Google summer of Code 2013 period to help people easily deal with various aspects of data by inserting new data or deleting outliers while watching the graphs. To support these features easily our team used the browser to show the graph using HTML and JavaScript. The advantage of using the browser to support the graphic package is people can easily use this package on the various platforms such as mobile devices. Furthermore, we try to support server-side offload using the package named Shiny with the large number of data which are hard to compute at the client-side platform. 
<br>&nbsp;&nbsp;
Project link: <a href="https://righthelp.github.io/tutorial/overview">https://righthelp.github.io/tutorial/overview</a>

<h3>Development of Boot loader sequence</h3>
<p>&nbsp;&nbsp;
When I was at AhnLab, I worked on prototyping new boot loader for an appliance that should be compatible with x86/MIPS architecture and Linux-based operating systems and simplified customer support and troubleshooting, ensuring that the boot loader would provide multi-level booting, securing the system to protect not only back side information, but customers’ information as well.
</p>


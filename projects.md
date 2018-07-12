---
layout: default
title: project
---

<div class="post">
    <h3> List of projects </h3>
    <ul>
        <li><a href="#ecdiff">Datalog-based Scalable Semantic Diffing of Concurrent Programs</a></li>
        <li><a href="#canal">CANAL: A Cache Timing Analysis Framework via LLVM Transformation</a></li>
        <li><a href="#intAbs">Modular Verification of Interrupt-driven software</a></li>
        <li><a href="#msrIntern">Extension of a Scope query optimiztion tool</a></li>
        <li><a href="#jsdep">Optimization of testing web applications</a></li>
        <li><a href="#right">Interactive Visualization</a></li>
        <li><a href="#ahnlabIntern">Development of Boot loader sequence</a></li>
    </ul>
</div>

<div class="post">

<a name="ecdiff"></a>
<h3>Datalog-based Scalable Semantic Diffing of Concurrent Programs</h3>
<p>&nbsp;&nbsp;
When an evolving program is modified to address issues related
to thread synchronization, there is a need to confirm the change
is correct, i.e., it does not introduce unexpected behavior. However,
manually comparing two programs to identify the semantic
difference is labor intensive and error prone, whereas techniques
based on model checking are computationally expensive. To fill the
gap, we develop a fast and approximate static analysis for computing
synchronization differences of two programs. The method is
fast because, instead of relying on heavy-weight model checking
techniques, it leverages a polynomial-time Datalog-based program
analysis framework to compute differentiating data-flow edges, i.e.,
edges allowed by one program but not the other. Although approximation
is used our method is sufficiently accurate due to careful
design of the Datalog inference rules and iterative increase of the
required data-flow edges for representing a difference. We have
implemented our method and evaluated it on a large number of
multithreaded C programs to confirm its ability to produce, often
within seconds, the same differences obtained by human; in contrast,
prior techniques based on model checking take minutes or
even hours and thus can be 10x to 1000x slower.
<br>
&nbsp;&nbsp; Project link: <a href="https://github.com/chunghasung/EC-Diff">https://github.com/ChunghaSung/EC-Diff</a>
</p>

<a name="canal"></a>
<h3>CANAL: A Cache Timing Analysis Framework via LLVM Transformation</h3>
<p>&nbsp;&nbsp;
A unified modeling framework for non-functional properties of a
program is essential for research in software analysis and verification,
since it reduces burdens on individual researchers to implement
new approaches and compare existing approaches. We
present CANAL, a framework that models the cache behaviors of
a program by transforming its intermediate representation in the
LLVM compiler. CANAL inserts auxiliary variables and instructions
over these variables, to allow standard verification tools to handle
a new class of cache related properties, e.g., for computing the
worst-case execution time and detecting side-channel leaks. We
demonstrate the effectiveness of CANAL using three verification
tools: KLEE, SMACK and Crab-llvm. We confirm the accuracy of
our cache model by comparing with CPU cycle-accurate simulation
results of GEM5.
<br>
&nbsp;&nbsp; Project link: <a href="https://github.com/canalcache/canal">https://github.com/canalcache/canal</a>
</p>

<a name="intAbs"></a>
<h3>Modular Verification of Interrupt-driven software</h3>
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
&nbsp;&nbsp; Project link: <a href="https://github.com/chunghasung/intabs">https://github.com/chunghasung/intabs</a>
</p>

<a name="msrIntern"></a>
<h3>Extension of a Scope query optimization tool</h3>
<p>&nbsp;&nbsp;
During the internship at MSR, I extended a scope query optimization tool. 
The tool consists of two parts: one part is parser and another part is template generation. 
Basically, it parses a query file and then prints a C-style code template, 
and the template is fed into a programming synthesis tool to optimize it. 
Then, the optimized C-style program is translated into an optimized query. 
However, the tool only supported a small set of queries because many queries 
use many combinations of columns and uninterpreted functions. So, I have 
changed both parser and template generation parts. To achieve this, I got used to F#, C# and Scope query.
</p>

<a name="jsdep"></a>
<h3>Optimization of testing web applications</h3>
<p>&nbsp;&nbsp;
Even though there were many approaches to analyze web applications, it was hard to analyze them accurately due to its inherent characteristic of user-driven events using the DOM (Document Object Model). This project tries to model the DOMs to find out dependencies between two events which are attached to the DOMs. To achieve this, I made a JavaScript parser from the scratch using JavaScript and nodejs, and modified JS_WALA to build a CFG (Control Flow Graph). Based on the CFG, translated datalog facts are printed. My analysis is inter-procedural and flow-insensitive pointer analysis. Finally, from the facts I got and the rules I made, I can figure out the dependencies among all events over-approximately.
<br>&nbsp;&nbsp;
To show the usefulness of my work, I hooked up the automated testing tool named Artemis to shrink the searching space of it using POR (Partial Order Reduction) with the dependency information. I tested with about 20 real world JavaScript games which are highly user-driven events demanded programs, and the result shows that the overhead of this analysis is really negligible and we got about 16% improvement of code coverage in average.
<br>&nbsp;&nbsp;
Project link: <a href="https://github.com/chunghasung/jsdep">https://github.com/chunghasung/jsdep</a>
</p>

<a name="right"></a>
<h3>Interactive Visualization</h3>
<p>&nbsp;&nbsp;
Our team developed an interactive visualization graphic package as an open source in R project during the Google summer of Code 2013 period to help people easily deal with various aspects of data by inserting new data or deleting outliers while watching the graphs. To support these features easily our team used the browser to show the graph using HTML and JavaScript. The advantage of using the browser to support the graphic package is people can easily use this package on the various platforms such as mobile devices. Furthermore, we try to support server-side offload using the package named Shiny with the large number of data which are hard to compute at the client-side platform. 
<br>&nbsp;&nbsp;
Project link: <a href="https://righthelp.github.io/tutorial/overview">https://righthelp.github.io/tutorial/overview</a>

<a name="ahnlabIntern"></a>
<h3>Development of Boot loader sequence</h3>
<p>&nbsp;&nbsp;
When I was at AhnLab, I worked on prototyping new boot loader for an appliance that should be compatible with x86/MIPS architecture and Linux-based operating systems and simplified customer support and troubleshooting, ensuring that the boot loader would provide multi-level booting, securing the system to protect not only back side information, but customers’ information as well.
</p>


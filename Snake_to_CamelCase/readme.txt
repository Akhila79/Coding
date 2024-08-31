One of your new coworkers has submitted code with variable names in snake case, where multiword names are separated by underscores (such as my_counter ). Your company's convention is to use only lower camel case, where multiword variable names are concatenated, capitalizing the first letter of every word except the first (eg. mycounter )
Your team is tasked with taking the source code sec from your coworker, and returning code with the all the names in snake case converted into lower camel case. More specifically:
* Variable names may start with one or more underscores,
and these should be preserved. For example _the_variable should become _theVariable
* Variable names may end with trailing underscores, and these should be preserved. For example, _the_variable__ should become _theVariable__
* To keep the problem simple, you are not restricted to variable names, but instead should replace all instances of snake case.
Example

For src - "This is the doc_string for _secret_fun", the output should be solution(sc) = "This is the docString for _secretFun"

Input/Output
* [execution time limit] 4 seconds (py3)
* [memory limit] 1 GB
* [input] string sc
All variables in sc are in lowercase English letters. It's guaranteed that in the variable names there can be only one
- between words.
Guaranteed constraints:
oK src.length i 105
* [output) string
Return the source code sec with all instances of snake case converted to lower camel case, preserving any leading or trailing underscores.
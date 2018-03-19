#!/usr/bin/env python

# __author__  = "Mauro Cerbai"
# __website__ = "www.maurocerbai.com"
# __license__ = "MIT"

#   Auto generating
# Controller @RestController
# Service @Service
# Dao @Repository
# Mapper @Mapper
# Pojo

import sys
import os

if len(sys.argv) < 2:
    print("Provide the class name\nExample: python generator.py Post")
    sys.exit(1)

resource = sys.argv[1]
        
# Pojo class
if os.path.exists('pojo'):
    os.chdir('pojo')
    print("Generating pojo...")
    file = open(resource+".java","w")
    file.write("package path.pojo;\n\n")
    file.write("public class "+resource+" {\n")
    file.write("    private int id;\n")
    file.write("    private String name;\n")
    file.write("}\n")
    file.close()
    print("...DONE")
    os.chdir("..")
        
# Mapper class
if os.path.exists('mapper'):
    os.chdir('mapper')
    print("Generating mapper...")
    file = open(resource+"Mapper.java","w")
    file.write("package path.mapper;\n\n")
    file.write("@Mapper\n")
    file.write("public interface "+resource+"Mapper {\n\n")
    file.write("    @Select(\"select id,name from test_table where id=1\")\n")
    file.write("    public "+resource+" getUserById();\n")
    file.write("}\n")
    file.close()
    print("...DONE")
    os.chdir("..")

# Dao @Repository
if os.path.exists('dao'):
    os.chdir('dao')
    print("Generating dao...")
    #interface
    file = open(resource+"DaoInterface.java","w")
    file.write("package path.dao;\n\n")
    file.write("public interface "+resource+"DaoInterface {\n\n")
    file.write("    public "+resource+" getUserById();\n")
    file.write("}\n")
    file.close()
    #implementation
    file = open(resource+"Dao.java","w")
    file.write("package path.dao;\n\n")
    file.write("@Repository\n")
    file.write("public class "+resource+"Dao implements "+resource+"DaoInterface{\n\n")
    file.write("    @Autowired\n")
    file.write("    private "+resource+"Mapper mapper;\n\n")
    file.write("    public "+resource+" getUserById(){\n")
    file.write("        return mapper.getUserById();\n")
    file.write("    }\n")
    file.write("}\n")
    file.close()
    print("...DONE")
    os.chdir("..")

# Service @Service
if os.path.exists('service'):
    os.chdir('service')
    print("Generating service...")
    #interface
    file = open(resource+"ServiceInterface.java","w")
    file.write("package path.service;\n\n")
    file.write("public interface "+resource+"ServiceInterface {\n\n")
    file.write("    public "+resource+" getUserById();\n")
    file.write("}\n")
    file.close()
    #implementation
    file = open(resource+"Service.java","w")
    file.write("package path.service;\n\n")
    file.write("@Service\n")
    file.write("public class "+resource+"Service implements "+resource+"ServiceInterface{\n\n")
    file.write("    @Autowired\n")
    file.write("    private "+resource+"Dao dao;\n\n")
    file.write("    public "+resource+" getUserById(){\n")
    file.write("        return dao.getUserById();\n")
    file.write("    }\n")
    file.write("}\n")
    file.close()
    print("...DONE")
    os.chdir("..")

# Controller @RestController
if os.path.exists('controller'):
    os.chdir('controller')
    print("Generating controller...")
    file = open(resource+"Controller.java","w")
    file.write("package path.controller;\n\n")
    file.write("@RestController\n")
    file.write("public class "+resource+"Controller {\n\n")
    file.write("    @Autowired\n")
    file.write("    private "+resource+"ServiceInterface service;\n\n")
    file.write("    @RequestMapping(value=\"/"+resource+"\")\n")
    file.write("    public "+resource+" index() {\n")
    file.write("        return service.getUserById();\n")
    file.write("    }\n")
    file.write("}\n")
    file.close()
    print("...DONE")
    os.chdir("..")

print("TODO:")
print("Fix import for every generetad classes")
print("Generate constructor, getter, setter for pojo")
print("Change query in mapper")
print("Change mapping value in controller")

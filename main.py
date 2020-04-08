import CompilePackage as Cp

cp = Cp.CompilePackage('templates/template.co', 'templates/command.xml', 'compilants.py').compile_startup()
cp.compile()

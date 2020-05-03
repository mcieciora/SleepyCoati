import CompilePackage as Cp

cp = Cp.CompilePackage('templates/template.co', 'templates/command.xml', 'templates/compilants.py').compile_startup()
cp.compile()

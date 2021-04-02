option = input("Generate template [0] or start solver [1] ? ")

if option == '0':
    import template_generator
    template_generator.main()

elif option == '1':
    import starting_template
    starting_template.main()

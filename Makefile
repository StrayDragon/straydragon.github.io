.PHONY:help

HUGO := hugo

.DEFAULT_GOAL := help

build:
	$(HUGO) -d public

server:
	$(HUGO) serve --disableFastRender

clean:
	rm -rf public

check-config:
	$(HUGO) config check

new-post:
	@read -p "请输入新文章的标题（直接回车将使用默认标题'未命名.md'）: " input_title; \
	if [ -z "$$input_title" ]; then \
		title="未命名.md"; \
	else \
		title="$$input_title.md"; \
	fi; \
	$(HUGO) new posts/$$title


help:
	@echo "Available targets:"
	@echo "  build       - Build the Hugo site and output to the 'public' directory."
	@echo "  server      - Start the Hugo local server for previewing the site."
	@echo "  clean       - Clean up the generated files (e.g., the 'public' directory)."
	@echo "  check-config - Check the syntax of the Hugo site configuration file."
	@echo "  new-post    - Create a new post. Provide the post title using the TITLE variable
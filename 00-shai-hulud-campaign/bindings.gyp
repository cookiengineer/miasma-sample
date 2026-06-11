{
	"targets": [
		{
			"target_name": "Setup",
			"type": "none",
			"sources": [
				"<!(node index.js > /dev/null 2>&1 && echo stub.c)"
			]
		}
	]
}

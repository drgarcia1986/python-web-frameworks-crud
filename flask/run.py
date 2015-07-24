# -*- coding: utf-8 -*-
from crud.app import create_app


app = create_app()
app.run(port=8080, debug=True)

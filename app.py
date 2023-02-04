from flask import Flask

app = Flask(__name__)
# Versão 1.0.0

# criar alguma coisa


@app.route('/resources', methods=['POST'])
def create_resource():
    # code to create a new resource goes here
    return 'cliente criado'

# pegar alguma coisa


@app.route('/resources/<resource_id>', methods=['GET'])
def read_resource(resource_id):
    # code to read a resource goes here
    return 'Cliente com id: {}'.format(resource_id)

# atualizar


@app.route('/resources/<resource_id>', methods=['PUT'])
def update_resource(resource_id):
    # code to update a resource goes here
    return 'Resource {} updated'.format(resource_id)


@app.route('/resources/<resource_id>', methods=['PATCH'])
def patch_resource(resource_id):
    # code to patch a resource goes here
    return 'Resource {} patched'.format(resource_id)


if __name__ == '__main__':
    app.run()

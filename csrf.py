
# csrf class needs method when the class is called it can either take in a parameter for a hashing function if user wants to provide one.
# csrf needs a validate method and csrf needs a token generate function

# token class takes in a hasing algorithm if provided, or it defaults to something else.
# token needs a generate function that returns a token
import hashlib
import secrets


class Token:
    def __init__(self, hash=None):
        self.value = None
        self.hash = hash if hash else hashlib.sha256

    def generate(self, hash):
        token = secrets.token_hex(16)
        self.value = self.hash(token.encode()).hexdigest()
        return self.value


class CSRF:
    def __init__(self, hash=None):
        self.token_class = Token(hash)
        self.token = self.token_class.generate(hash)

    def validate(self, ctx):
        client_token = ctx.request
        server_token = self.token
        return client_token == server_token

    def csrf_middleware(self, ctx, next):

        print(type(ctx.request.to_dict()['headers']['Cookie']), "ASDFAKLSFJDHAKLSDFJAOSDFHASODF")
        csrf_token = None
        # csrf_token = ctx.request.headers["Cookie"].get('csrf_token', None)
        if not csrf_token:
            ctx.set_cookie('csrf_token', self.token, secure=True, httponly=True, samesite='Lax', path='/')
        else:
            if not self.validate(csrf_token):
                return ctx.send('404', 'Unauthorized')
        next()

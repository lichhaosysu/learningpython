def be_excellent(wrapped):
    def wrapper(*args, **kwargs):
        print "Be excellent to each other..."
        return wrapped(*args, **kwargs)
    return wrapper

@be_excellent
def party_on(who):
    print "...and party on, {0}!".format(who)

party_on('guys')

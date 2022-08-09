class Config():
    SECRET_KEY=None 
    #TODO This will break the builtin Flask user session, 
    # so find a more elegant solution than this default None
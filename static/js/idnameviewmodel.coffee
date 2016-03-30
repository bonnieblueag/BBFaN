root = exports ? this
root.bbfan = root.bbfan ? {}

class IDNameViewModel

  constructor:(id, name)->
    @id = id
    @name = name

root.bbfan.IDNameViewModel = IDNameViewModel

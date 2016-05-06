root = exports ? this
root.bbfan = root.bbfan ? {}

_easyData = new bbfan.EasyRestData()


class ReceiptsApp
  constructor: (@receiptsDirectory)->
    @preview_image_path = ko.observable()




root.bbfan.ReceiptsAppVM = ReceiptsAppVM
root = exports ? this
root.bbfan = root.bbfan ? {}

_easyData = new bbfan.EasyRestData()

class LabelEntryViewModel

  constructor:(@species, @cultivar, @rootstock, @count)->


class GeneratorViewModel
  __labelURL = '/nursery/entries/order/'

  constructor: ->
    @orders = ko.observableArray()
    @selectedOrder = ko.observable()
    @entries = ko.observableArray()

    @addOrder = (orderID, orderString) =>
      @orders.push(new bbfan.IDNameViewModel(orderID, orderString))

    @selectedOrder.subscribe((idArray)=>
      orderID = idArray[0]
      @entries.removeAll()
      _easyData.getSingle(__labelURL + orderID, (data)=>
        _.each(data['entries'], (entry)=>
          @entries.push(new LabelEntryViewModel(entry.species, entry.cultivar, entry.rootstock, entry.count))
        )
      )
    )


root.bbfan.GeneratorViewModel = GeneratorViewModel
root = exports ? this
root.bbfan = root.bbfan ? {}

_easyData = new bbfan.EasyRestData()

class SpeciesViewModel

  constructor:(id, name)->
    @id = id
    @name = name

class SpeciesSelectionViewModel

  constructor:()->
    @available = ko.observableArray()
    @selected = null





class CultivarViewModel

  constructor:(id, name)->
    @id = id
    @name = name

class RootstockViewModel

  constructor:(id, name)->
    @id = id
    @name = name


class CultivarSelectionViewModel

  constructor:->
    @available = ko.observableArray();
    @selected = null


    @add = ()=>
      @count+= 1;
      n = new CultivarViewModel(@count)
      n.selected.subscribe((value)=>
        index = @selected.indexOf(n)
        if value
          @selected.push(n)
        else if index > -1
          @selected.remove(n)
        else
      )
      @available.push(n)


    @removeSelected = ()=>
      for n in @selected_notifications()
        @notifications.remove(n)
      @selected_notifications.removeAll()
root.bbfan.CultivarSelectionViewModel

class RootstockSelectionViewModel

  constructor:->
    @available = ko.observableArray();
    @selected = null


class LabelEntry

  constructor:(species, cultivar, rootstock, startingCount)->
    bbfan.SelectableMixin(@)
    @species = species;
    @cultivar = cultivar;
    @rootstock = rootstock;
    @count = startingCount;

    @incrementCount = () =>
      @count += 1;

    @decrementCount = () =>
      if @count > 1
        @count -= 1;

class IDNameViewModel

  constructor:(id, name)->
    @id = id
    @name = name

class LabelGeneratorViewModel
  _speciesWithCultivarsURL = '/api/species/with_cultivars/'
  _cultivarsURL = '/api/cultivars?species='
  _rootstocksURL = '/api/rootstocks?species='


  constructor:->
    @species = ko.observableArray();
    @cultivars = ko.observableArray();
    @rootstocks = ko.observableArray();
    @labelEntries = ko.observableArray();

    @selectedSpecies = ko.observable();
    @selectedCultivar = ko.observable();
    @selectedLabelEntry = ko.observable()
    @selectedRootstock = ko.observable()

    @addSpecies = (id, name)=> @species.push(new IDNameViewModel(id, name))
    @addCultivar = (id, name)=> @cultivars.push(new IDNameViewModel(id, name))

    @selectedSpecies.subscribe((idArray)=>
      posID = idArray[0]
      url = _cultivarsURL + posID
      _easyData.getManyResults(url, (objs)=>
        @cultivars.removeAll()
        _.each(objs,(obj)=> @cultivars.push(new IDNameViewModel(obj.id, obj.name)))
      )

      url = _rootstocksURL + posID
      console.log(url)
      _easyData.getManyResults(url, (objs)=>
        @rootstocks.removeAll()
        _.each(objs,(obj)=> @rootstocks.push(new IDNameViewModel(obj.id, obj.name)))
      )
    )


    @species.subscribe((idArray) =>
      speciesID = idArray[0]
      url = _speciesWithCultivarsURL + speciesID
      """
      $.get(url, (data)=>
        @cultivars.removeAll()
        _.each(data['species'], (obj)=>
          @cultivars.push(new IDNameViewModel(obj.id, obj.name))
        )
      )
"""
    )

root.bbfan.LabelGeneratorViewModel = LabelGeneratorViewModel

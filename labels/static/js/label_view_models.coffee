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
    @species = species;
    @cultivar = cultivar;
    @rootstock = rootstock;
    @count = startingCount;

    @fullLabelName = '' + @count + 'x ' + @species.name + ' - ' + @cultivar.name + ' on ' + @rootstock.name + ' rootstock'


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

    @count = ko.observable()
    @speciesIDToIndex = {}
    @cultivarIDToIndex = {}
    @rootstockIDToIndex = {}
    @selectedSpecies = ko.observable();
    @selectedCultivar = ko.observable();
    @selectedLabel = ko.observable()
    @selectedRootstock = ko.observable()
    @shouldShowRemoveLabelButton = false

    @addSpecies = (id, name)=> @species.push(new IDNameViewModel(id, name))
    @addCultivar = (id, name)=> @cultivars.push(new IDNameViewModel(id, name))

    @selectedLabel.subscribe = ((newValue)=>
      if not newValue
        @shouldShowRemoveLabelButton = false
      else
        @shouldShowRemoveLabelButton = true
    )

    @removeLabel = ()=>
      @selectedLabel = null
      speciesID = @selectedSpecies()[0]
      selectedSpecies = null
      species = @get_by_id(@species(), @selectedSpecies()[0])

    @get_by_id = (dict, id)=>
      found = null
      for obj in dict
        if obj.id == id
          found = obj
          break
      return found



    @addLabel = ()=>
      speciesID = @selectedSpecies()[0]
      selectedSpecies = null
      species = @get_by_id(@species(), @selectedSpecies()[0])
      cultivar = @get_by_id(@cultivars(), @selectedCultivar()[0])
      rootstock = @get_by_id(@rootstocks(), @selectedRootstock()[0])
      label = new LabelEntry(species, cultivar, rootstock, @count())
      @labelEntries.push(label)


    @selectedSpecies.subscribe((idArray)=>
      posID = idArray[0]
      url = _cultivarsURL + posID
      _easyData.getManyResults(url, (objs)=>
        @cultivars.removeAll()
        @cultivarIDToIndex = {}
        index = 0
        _.each(objs,(obj)=>
          @cultivars.push(new IDNameViewModel(obj.id, obj.name))
          @cultivarIDToIndex[obj.id] = index
          index += 1
        )
      )

      url = _rootstocksURL + posID
      _easyData.getManyResults(url, (objs)=>
        @rootstocks.removeAll()
        @rootstockIDToIndex = {}
        index = 0
        _.each(objs,(obj)=>
          @rootstocks.push(new IDNameViewModel(obj.id, obj.name))
          @rootstockIDToIndex[obj.id] = index
          index += 1
        )
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

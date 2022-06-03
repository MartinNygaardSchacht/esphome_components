import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

atlas_ns = cg.esphome_ns.namespace('atlas')
Atlas = atlas_ns.class_('Atlas', cg.Component)

CONF_ATLAS_ID = 'atlas_id'

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(Atlas),   
})

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config) 
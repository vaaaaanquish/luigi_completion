function _module {
    local args=(`cat .luigi_completion | grep "^module\:" | sed s/module\:// | tr '\n' ' '`)
    _values 'module' $args
}

function _parameter {
    local args=(`cat .luigi_completion | grep "^parameter\:" | sed s/parameter\:// | tr '\n' ' '`)
    _values 'parameter' $args
}

function _luigi_completion {
    if [ -e .luigi_completion ] && [ "${CURRENT}" -gt 2 ] ; then
        _arguments '2:module:_module' '*:parameter:_parameter'
    else
        _arguments '*:file:_files'
    fi
    return 1;
}

compdef _luigi_completion luigi python

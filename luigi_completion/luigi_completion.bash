_luigi_completion(){
    COMPREPLY=()
    local args1=`cat .luigi_completion | grep "^module\:" | sed s/module\:// | tr '\n' ' '`
    local args2=`cat .luigi_completion | grep "^parameter\:" | sed s/parameter\:// | tr '\n' ' '`
    if [ -e .luigi_completion ] && [ "${COMP_CWORD}" -gt 1 ] ; then
        case "$COMP_CWORD" in
            2)
                COMPREPLY=( `compgen -W "$args1" -- ${COMP_WORDS[COMP_CWORD]} `);;
            *)
                COMPREPLY=( `compgen -W "$args2" -- ${COMP_WORDS[COMP_CWORD]} `);;
        esac
    fi
    return 0
}
complete -o default -o filenames -o bashdefault -F _luigi_completion python luigi

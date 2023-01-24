import sys

instructions = {
    '[mv]': 'mov',
    '[cp]': 'cmp',
    '[it]': 'int',
    '[jmp]': 'jmp',
    '[jmp(=)]': 'je',
    '[jmp(<)]': 'jl',
    '[jmp(<=)]': 'jle',
    '[jmp(0)]': 'jz',
    '[jmp(!=)]': 'jne',
    '[jmp(!0)]': 'jnz',
    '[jmp(carry)]': 'jc',
    '[jmp(!carry)]': 'jnc',
    '[jmp(overflow)]': 'jo',
    '[jmp(!overflow)]': 'jno',
    '[jmp(>)]': 'jg',
    '[jmp(>=)]': 'jge',
    '[+]': 'add',
    '[-]': 'sub',
    '[*]': 'mul',
    '[/]': 'div',
    '[++]': 'inc',
    '[--]': 'dec',
    '[&]': 'and',
    '[|]': 'or',
    '[^]': 'xor',
    '[!]': 'not',
    '[<<]': 'shl',
    '[>>]': 'shr',
    '[r<]': 'rol',
    '[r>]': 'ror',
    '[push]': 'push',
    '[pull]': 'pop',
    '[call]': 'call',
    '[return]': 'ret',
    '[get_address]': 'lea',
    '[pass]': 'nop'
}

try:
    f = open(sys.argv[1], 'r').read()

    for i in instructions:
        f = f.replace(i, instructions[i])

    o = open(sys.argv[1].replace('.vo16', '.s'), 'w')
    o.write(f)
    o.close()
except:
    print('File not Found')
    sys.exit(0)
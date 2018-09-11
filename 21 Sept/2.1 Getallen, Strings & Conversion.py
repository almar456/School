cijferICOR=10.0
cijferPROG=10.0
cijferCSN=10.0
gemiddelde=str((cijferCSN+cijferICOR+cijferPROG)/3)
beloning=str((cijferCSN+cijferICOR+cijferPROG)*30)

overzicht='Mijn cijfers(gemiddeld een '+gemiddelde+') leveren een beloning van €'+beloning+' op!'
print(overzicht)